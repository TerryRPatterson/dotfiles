"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const ts = require("typescript");
const path = require("path");
const embeddedSupport_1 = require("../embeddedSupport");
const vscode_languageserver_types_1 = require("vscode-languageserver-types");
function isVue(filename) {
    return path.extname(filename) === '.vue';
}
exports.isVue = isVue;
function parseVue(text) {
    const doc = vscode_languageserver_types_1.TextDocument.create('test://test/test.vue', 'vue', 0, text);
    const regions = embeddedSupport_1.getDocumentRegions(doc);
    const script = regions.getEmbeddedDocumentByType('script');
    return script.getText() || 'export default {};';
}
exports.parseVue = parseVue;
function createUpdater(tsModule) {
    const clssf = tsModule.createLanguageServiceSourceFile;
    const ulssf = tsModule.updateLanguageServiceSourceFile;
    const scriptKindTracker = new WeakMap();
    function isTSLike(scriptKind) {
        return scriptKind === ts.ScriptKind.TS || scriptKind === ts.ScriptKind.TSX;
    }
    return {
        createLanguageServiceSourceFile(fileName, scriptSnapshot, scriptTarget, version, setNodeParents, scriptKind) {
            const sourceFile = clssf(fileName, scriptSnapshot, scriptTarget, version, setNodeParents, scriptKind);
            scriptKindTracker.set(sourceFile, scriptKind);
            if (isVue(fileName) && !isTSLike(scriptKind)) {
                modifyVueSource(tsModule, sourceFile);
            }
            return sourceFile;
        },
        updateLanguageServiceSourceFile(sourceFile, scriptSnapshot, version, textChangeRange, aggressiveChecks) {
            const scriptKind = scriptKindTracker.get(sourceFile);
            sourceFile = ulssf(sourceFile, scriptSnapshot, version, textChangeRange, aggressiveChecks);
            if (isVue(sourceFile.fileName) && !isTSLike(scriptKind)) {
                modifyVueSource(tsModule, sourceFile);
            }
            return sourceFile;
        }
    };
}
exports.createUpdater = createUpdater;
function modifyVueSource(tsModule, sourceFile) {
    const exportDefaultObject = sourceFile.statements.find(st => st.kind === tsModule.SyntaxKind.ExportAssignment &&
        st.expression.kind === tsModule.SyntaxKind.ObjectLiteralExpression);
    if (exportDefaultObject) {
        // 1. add `import Vue from 'vue'
        //    (the span of the inserted statement must be (0,0) to avoid overlapping existing statements)
        const setZeroPos = getWrapperRangeSetter(tsModule, { pos: 0, end: 0 });
        const vueImport = setZeroPos(tsModule.createImportDeclaration(undefined, undefined, setZeroPos(tsModule.createImportClause(tsModule.createIdentifier('__vueEditorBridge'), undefined)), setZeroPos(tsModule.createLiteral('vue-editor-bridge'))));
        const statements = sourceFile.statements;
        statements.unshift(vueImport);
        // 2. find the export default and wrap it in `__vueEditorBridge(...)` if it exists and is an object literal
        // (the span of the function construct call and *all* its members must be the same as the object literal it wraps)
        const objectLiteral = exportDefaultObject.expression;
        const setObjPos = getWrapperRangeSetter(tsModule, objectLiteral);
        const vue = tsModule.setTextRange(tsModule.createIdentifier('__vueEditorBridge'), {
            pos: objectLiteral.pos,
            end: objectLiteral.pos + 1
        });
        exportDefaultObject.expression = setObjPos(tsModule.createCall(vue, undefined, [objectLiteral]));
        setObjPos(exportDefaultObject.expression.arguments);
    }
}
/** Create a function that calls setTextRange on synthetic wrapper nodes that need a valid range */
function getWrapperRangeSetter(tsModule, wrapped) {
    return (wrapperNode) => tsModule.setTextRange(wrapperNode, wrapped);
}
//# sourceMappingURL=preprocess.js.map
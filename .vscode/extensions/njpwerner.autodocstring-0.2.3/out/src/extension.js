'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
const vs = require("vscode");
const autodocstring_1 = require("./autodocstring");
function activate(context) {
    context.subscriptions.push(vs.commands.registerCommand('extension.generateDocstring', () => {
        let editor = vs.window.activeTextEditor;
        let autoDocstring = new autodocstring_1.AutoDocstring(editor);
        autoDocstring.generateDocstring(false);
    }));
    let config = vs.workspace.getConfiguration("autoDocstring");
    if (config.get('generateDocstringOnEnter')) {
        context.subscriptions.push(vs.workspace.onDidChangeTextDocument(changeEvent => { activateOnEnter(changeEvent); }));
    }
    ;
}
exports.activate = activate;
function activateOnEnter(changeEvent) {
    if (vs.window.activeTextEditor.document !== changeEvent.document)
        return;
    if (changeEvent.contentChanges.length < 1)
        return;
    if (changeEvent.contentChanges[0].rangeLength !== 0)
        return;
    if (changeEvent.contentChanges[0].text.replace(/ |\t|\r/g, "") === "\n") {
        processEnter(changeEvent);
    }
}
function processEnter(changeEvent) {
    let editor = vs.window.activeTextEditor;
    let range = getPrecedingRange(3, changeEvent);
    if (editor.document.getText(range) === '"""') {
        let autoDocstring = new autodocstring_1.AutoDocstring(editor, '"""');
        autoDocstring.generateDocstring(true);
    }
    else if (editor.document.getText(range) === "'''") {
        let autoDocstring = new autodocstring_1.AutoDocstring(editor, "'''");
        autoDocstring.generateDocstring(true);
    }
}
function getPrecedingRange(numberOfChars, changeEvent) {
    let position = changeEvent.contentChanges[0].range.end;
    let range = new vs.Range(position.translate(0, -1 * numberOfChars), position);
    return range;
}
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map
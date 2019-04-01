"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const vs = require("vscode");
function inArray(item, array) {
    return array.some(x => item == x);
}
exports.inArray = inArray;
function includesFromArray(string, substrings) {
    substrings.some(x => string.includes(x));
}
exports.includesFromArray = includesFromArray;
function deleteRange(range) {
    const ws_edit = new vs.WorkspaceEdit();
    const editor = vs.window.activeTextEditor;
    ws_edit.delete(editor.document.uri, range);
    vs.workspace.applyEdit(ws_edit);
}
exports.deleteRange = deleteRange;
function deleteLine(line_num) {
    const editor = vs.window.activeTextEditor;
    const line = editor.document.lineAt(line_num);
    const ws_edit = new vs.WorkspaceEdit();
    ws_edit.delete(editor.document.uri, line.rangeIncludingLineBreak);
    vs.workspace.applyEdit(ws_edit);
}
exports.deleteLine = deleteLine;
//# sourceMappingURL=utils.js.map
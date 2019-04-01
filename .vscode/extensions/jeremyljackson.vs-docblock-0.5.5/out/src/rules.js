"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const vscode_1 = require("vscode");
/**
 * Defines on enter rules for auto completed `*` character in docblocks. This
 * is not support by vscode in all languages
 */
class Rules {
}
Rules.enterRules = [
    {
        action: {
            appendText: ' * ',
            indentAction: vscode_1.IndentAction.None,
        },
        afterText: /^\s*\*\/$/,
        beforeText: /^\s*\/\*\*(?!\/)([^\*]|\*(?!\/))*/gm,
    }, {
        action: {
            appendText: ' * ',
            indentAction: vscode_1.IndentAction.None,
        },
        beforeText: /^\s*\/\*\*(?!\/)([^\*]|\*(?!\/))*$/,
    }, {
        action: {
            appendText: ' * ',
            indentAction: vscode_1.IndentAction.Outdent,
        },
        beforeText: /^(\t|(\s))*\s\*(\s([^\*]|\*(?!\/))*)?$/,
    },
];
exports.Rules = Rules;
//# sourceMappingURL=rules.js.map
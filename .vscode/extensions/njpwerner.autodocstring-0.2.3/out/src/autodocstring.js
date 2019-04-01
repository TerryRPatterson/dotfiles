"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const vs = require("vscode");
const factories = require("./docstring_factories/factories");
const parse_1 = require("./parse/parse");
const closed_docstring_1 = require("./parse/closed_docstring");
const multi_line_string_1 = require("./parse/multi_line_string");
class AutoDocstring {
    constructor(editor, quoteStyle = null) {
        this.editor = editor;
        this.quoteStyle = quoteStyle || vs.workspace.getConfiguration("autoDocstring").get("quoteStyle").toString();
        let docstringFormat = vs.workspace.getConfiguration("autoDocstring").get("docstringFormat");
        switch (docstringFormat) {
            case "google":
                this.docstringFactory = new factories.GoogleFactory(this.quoteStyle);
                break;
            case "sphinx":
                this.docstringFactory = new factories.SphinxFactory(this.quoteStyle);
                break;
            case "numpy":
                this.docstringFactory = new factories.NumpyFactory(this.quoteStyle);
                break;
            default:
                this.docstringFactory = new factories.DefaultFactory(this.quoteStyle);
        }
    }
    generateDocstring(onEnter) {
        let document = this.editor.document.getText();
        let position = this.editor.selection.active;
        let linePosition = position.line;
        let charPosition = position.character;
        if (!onEnter) {
        }
        // Check whether the docstring is already closed for enter activation
        if (!onEnter || this.validEnterActivation(document, linePosition, charPosition)) {
            let docstringParts = parse_1.parse(document, linePosition);
            let docstringSnippet = this.docstringFactory.createDocstring(docstringParts, !onEnter);
            this.editor.insertSnippet(docstringSnippet, position);
        }
    }
    validEnterActivation(document, linePosition, charPosition) {
        console.log("multiline: ", multi_line_string_1.isMultiLineString(document, linePosition, charPosition, this.quoteStyle));
        console.log("closed: ", closed_docstring_1.docstringIsClosed(document, linePosition, charPosition, this.quoteStyle));
        return (!multi_line_string_1.isMultiLineString(document, linePosition, charPosition, this.quoteStyle) &&
            !closed_docstring_1.docstringIsClosed(document, linePosition, charPosition, this.quoteStyle));
    }
}
exports.AutoDocstring = AutoDocstring;
//# sourceMappingURL=autodocstring.js.map
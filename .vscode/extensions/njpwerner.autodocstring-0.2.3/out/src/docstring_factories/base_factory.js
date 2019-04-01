"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const docstring_parts_1 = require("../docstring_parts");
const vscode = require("vscode");
class BaseFactory {
    constructor(quoteStyle) {
        this._snippet = new vscode.SnippetString();
        this._quoteStyle = quoteStyle;
        let config = vscode.workspace.getConfiguration("autoDocstring");
        this._newlineBeforeSummary = config.get("newlineBeforeSummary") === true;
        this._includeDescription = config.get("includeDescription") === true;
        this._includeName = config.get("includeName") === true;
        this._guessTypes = config.get("guessTypes") === true;
    }
    createDocstring(docstring, openingQuotes) {
        this._snippet.value = "";
        if (this._newlineBeforeSummary) {
            this._snippet.appendText("\n");
        }
        this.generateSummary(docstring);
        if (this._includeDescription) {
            this.generateDescription();
        }
        if (!this._guessTypes) {
            docstring_parts_1.removeTypes(docstring);
        }
        docstring_parts_1.addTypePlaceholders(docstring, '[type]');
        if (docstring != undefined) {
            if (docstring.decorators.length > 0) {
                this.formatDecorators(docstring.decorators);
            }
            if (docstring.args.length > 0) {
                this.formatArguments(docstring);
            }
            if (docstring.kwargs.length > 0) {
                this.formatKeywordArguments(docstring);
            }
            if (docstring.raises.length > 0) {
                this.formatRaises(docstring.raises);
            }
            if (docstring.returns != undefined) {
                this.formatReturns(docstring.returns);
            }
        }
        this.commentText(openingQuotes);
        return this._snippet;
    }
    commentText(openingQuotes) {
        if (openingQuotes) {
            this._snippet.value = this._quoteStyle + this._snippet.value + this._quoteStyle;
        }
        else {
            this._snippet.value = this._snippet.value + this._quoteStyle;
        }
    }
    appendText(text) {
        this._snippet.appendText(text);
    }
    appendPlaceholder(text) {
        this._snippet.appendPlaceholder(text);
    }
    appendNewLine() {
        this._snippet.appendText("\n");
    }
}
exports.BaseFactory = BaseFactory;
//# sourceMappingURL=base_factory.js.map
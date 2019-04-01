"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const base_factory_1 = require("./base_factory");
class GoogleFactory extends base_factory_1.BaseFactory {
    generateSummary(docstring) {
        if (this._includeName) {
            this._snippet.appendText(`${docstring.name} `);
        }
        this._snippet.appendPlaceholder("[summary]");
        this.appendNewLine();
    }
    generateDescription() {
        this.appendNewLine();
        this._snippet.appendPlaceholder("[description]");
        this.appendNewLine();
    }
    formatDecorators(decorators) {
        this.appendText("\nDecorators:\n");
        for (let decorator of decorators) {
            this.appendText(`\t${decorator.name}\n`);
        }
    }
    formatArguments(docstring) {
        if (docstring.args.length > 0 || docstring.kwargs.length > 0) {
            this.appendText("\nArgs:\n");
        }
        for (let arg of docstring.args) {
            this.appendText(`\t${arg.var} (`);
            this.appendPlaceholder(`${arg.type}`);
            this.appendText("): ");
            this.appendPlaceholder("[description]");
            this.appendNewLine();
        }
    }
    formatKeywordArguments(docstring) {
        for (let kwarg of docstring.kwargs) {
            this.appendText(`\t${kwarg.var} (`);
            this.appendPlaceholder(`${kwarg.type}`);
            this.appendText(`, optional): Defaults to ${kwarg.default}. `);
            this.appendPlaceholder("[description]");
            this.appendNewLine();
        }
    }
    formatRaises(raises) {
        this.appendText("\nRaises:\n");
        for (let raise of raises) {
            this.appendText(`\t${raise.exception}: `);
            this.appendPlaceholder("[description]");
            this.appendNewLine();
        }
    }
    formatReturns(returns) {
        this.appendText("\nReturns:\n");
        this.appendText("\t");
        this.appendPlaceholder(`${returns.type}`);
        this.appendText(": ");
        this.appendPlaceholder("[description]");
        this.appendNewLine();
    }
}
exports.GoogleFactory = GoogleFactory;
//# sourceMappingURL=google.js.map
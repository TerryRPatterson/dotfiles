"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const base_factory_1 = require("./base_factory");
class SphinxFactory extends base_factory_1.BaseFactory {
    generateSummary(docstring) {
        if (this._includeName) {
            this._snippet.appendText(`${docstring.name} `);
        }
        this._snippet.appendPlaceholder("[summary]");
        this.appendNewLine();
        this.appendNewLine();
    }
    generateDescription() {
        this._snippet.appendPlaceholder("[description]");
        this.appendNewLine();
        this.appendNewLine();
    }
    formatDecorators(decorators) {
        // I need to find an example of decorators in sphinx format
    }
    formatArguments(docstring) {
        for (let arg of docstring.args) {
            this.appendText(":param " + arg.var + ": ");
            this.appendPlaceholder("[description]");
            this.appendNewLine();
            this.appendText(":type " + arg.var + ": ");
            this.appendPlaceholder(`${arg.type}`);
            this.appendNewLine();
        }
    }
    formatKeywordArguments(docstring) {
        for (let kwarg of docstring.kwargs) {
            this.appendText(":param " + kwarg.var + ": ");
            this.appendPlaceholder("[description]");
            this.appendText(", defaults to " + kwarg.default);
            this.appendNewLine();
            this.appendText(":param " + kwarg.var + ": ");
            this.appendPlaceholder(`${kwarg.type}`);
            this.appendText(", optional");
            this.appendNewLine();
        }
    }
    formatRaises(raises) {
        for (let raise of raises) {
            this.appendText(":raises " + raise.exception + ": ");
            this.appendPlaceholder("[description]");
            this.appendNewLine();
        }
    }
    formatReturns(returns) {
        this.appendText(":return: ");
        this.appendPlaceholder("[description]");
        this.appendNewLine();
        this.appendText(":rtype: ");
        this.appendPlaceholder(`${returns.type}`);
        this.appendNewLine();
    }
}
exports.SphinxFactory = SphinxFactory;
//# sourceMappingURL=sphinx.js.map
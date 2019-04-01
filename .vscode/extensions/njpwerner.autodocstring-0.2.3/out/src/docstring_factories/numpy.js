"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const base_factory_1 = require("./base_factory");
class NumpyFactory extends base_factory_1.BaseFactory {
    generateSummary(docstring) {
        if (this._includeName) {
            this._snippet.appendText(`${docstring.name}\n\n`);
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
        // I need to find an example of decorators in numpy format
    }
    formatArguments(docstring) {
        if (docstring.args.length > 0 || docstring.kwargs.length > 0) {
            this.appendText("Parameters\n----------\n");
        }
        for (let arg of docstring.args) {
            this.appendText(arg.var + " : ");
            this.appendPlaceholder(`${arg.type}`);
            this.appendText("\n");
            this.appendText("\t");
            this.appendPlaceholder("[description]");
            this.appendNewLine();
        }
        if (!docstring.kwargs.length) {
            this.appendNewLine();
        }
    }
    formatKeywordArguments(docstring) {
        if (!docstring.args.length) {
            this.appendText("Parameters\n----------\n");
        }
        for (let kwarg of docstring.kwargs) {
            this.appendText(kwarg.var + " : ");
            this.appendPlaceholder(`${kwarg.type}`);
            this.appendText(", optional\n");
            this.appendText("\t");
            this.appendPlaceholder("[description]");
            this.appendText(" (the default is " + kwarg.default + ", which ");
            this.appendPlaceholder("[default_description]");
            this.appendText(")\n");
        }
        this.appendNewLine();
    }
    formatRaises(raises) {
        this.appendText("Raises\n------\n");
        for (let raise of raises) {
            this.appendText(raise.exception + "\n\t");
            this.appendPlaceholder("[description]");
            this.appendNewLine();
        }
        this.appendNewLine();
    }
    formatReturns(returns) {
        this.appendText("Returns\n-------\n");
        this.appendPlaceholder(`${returns.type}`);
        this.appendText("\n\t");
        this.appendPlaceholder("[description]");
        this.appendNewLine();
    }
}
exports.NumpyFactory = NumpyFactory;
//# sourceMappingURL=numpy.js.map
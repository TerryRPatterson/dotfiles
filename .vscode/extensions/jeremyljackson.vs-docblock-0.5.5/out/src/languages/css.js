/**
 * Css specific language parser
 */
'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
const parser_1 = require("../parser");
class Css extends parser_1.Parser {
    /**
     * Constructs settings specific to Css
     */
    constructor() {
        super({
            grammar: {
                class: '',
                function: '',
                identifier: '[a-zA-Z_$0-9]',
                modifiers: [],
                types: [],
                variables: [],
            },
        });
    }
}
exports.Css = Css;
//# sourceMappingURL=css.js.map
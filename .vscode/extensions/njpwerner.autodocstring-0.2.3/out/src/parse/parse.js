"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const get_lines_1 = require("./get_lines");
const parse_parameters_1 = require("./parse_parameters");
const tokenize_definition_1 = require("./tokenize_definition");
const get_function_name_1 = require("./get_function_name");
function parse(document, positionLine) {
    let definition = get_lines_1.getDefinition(document, positionLine);
    let body = get_lines_1.getBody(document, positionLine);
    let parameterTokens = tokenize_definition_1.tokenizeDefinition(definition);
    let functionName = get_function_name_1.getFunctionName(definition);
    return parse_parameters_1.parseParameters(parameterTokens, body, functionName);
}
exports.parse = parse;
//# sourceMappingURL=parse.js.map
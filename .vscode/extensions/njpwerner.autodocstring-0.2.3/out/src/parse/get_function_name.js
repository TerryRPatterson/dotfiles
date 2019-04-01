"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function getFunctionName(functionDefinition) {
    let pattern = /(?:def|class)\s+(\w+)\s*\(/;
    let match = pattern.exec(functionDefinition);
    if (match == undefined || match[1] == undefined) {
        return "";
    }
    ;
    return match[1];
}
exports.getFunctionName = getFunctionName;
//# sourceMappingURL=get_function_name.js.map
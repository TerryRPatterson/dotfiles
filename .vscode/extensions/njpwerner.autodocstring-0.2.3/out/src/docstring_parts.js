"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function removeTypes(docstringParts) {
    for (let arg of docstringParts.args) {
        arg.type = undefined;
    }
    for (let kwarg of docstringParts.kwargs) {
        kwarg.type = undefined;
    }
    docstringParts.returns.type = undefined;
}
exports.removeTypes = removeTypes;
function addTypePlaceholders(docstringParts, placeholder) {
    for (let arg of docstringParts.args) {
        if (arg.type == undefined) {
            arg.type = placeholder;
        }
    }
    for (let kwarg of docstringParts.kwargs) {
        if (kwarg.type == undefined) {
            kwarg.type = placeholder;
        }
    }
    let returns = docstringParts.returns;
    if (returns != undefined && returns.type == undefined) {
        returns.type = placeholder;
    }
}
exports.addTypePlaceholders = addTypePlaceholders;
//# sourceMappingURL=docstring_parts.js.map
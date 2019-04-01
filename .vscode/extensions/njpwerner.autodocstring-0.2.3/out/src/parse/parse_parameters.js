"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const guess_types_1 = require("./guess_types");
function parseParameters(parameterTokens, body, functionName) {
    return {
        name: functionName,
        decorators: parseDecorators(parameterTokens),
        args: parseArguments(parameterTokens),
        kwargs: parseKeywordArguments(parameterTokens),
        returns: parseReturn(parameterTokens, body),
        raises: parseRaises(body),
    };
}
exports.parseParameters = parseParameters;
function parseDecorators(parameters) {
    let decorators = [];
    let pattern = /^@(\w+)/;
    for (let param of parameters) {
        let match = param.trim().match(pattern);
        if (match == undefined) {
            continue;
        }
        decorators.push({
            name: match[1],
        });
    }
    return decorators;
}
function parseArguments(parameters) {
    let args = [];
    let excludedArgs = ['self', 'cls'];
    let pattern = /^(\w+)/;
    for (let param of parameters) {
        let match = param.trim().match(pattern);
        if (match == undefined || param.includes('=') || inArray(param, excludedArgs)) {
            continue;
        }
        args.push({
            var: match[1],
            type: guess_types_1.guessType(param),
        });
    }
    return args;
}
function parseKeywordArguments(parameters) {
    let kwargs = [];
    let pattern = /^(\w+)(?:\s*:[^=]+)?\s*=\s*(.+)/;
    for (let param of parameters) {
        let match = param.trim().match(pattern);
        if (match == undefined) {
            continue;
        }
        kwargs.push({
            var: match[1],
            default: match[2],
            type: guess_types_1.guessType(param),
        });
    }
    return kwargs;
}
function parseReturn(parameters, body) {
    let returnType = parseReturnFromDefinition(parameters);
    if (returnType == undefined) {
        return parseReturnFromBody(body);
    }
    return returnType;
}
function parseReturnFromDefinition(parameters) {
    let pattern = /^->\s*([\w\[\], \.]*)/;
    for (let param of parameters) {
        let match = param.trim().match(pattern);
        if (match == undefined) {
            continue;
        }
        return { type: match[1] };
    }
    return undefined;
}
function parseReturnFromBody(body) {
    let pattern = /return /;
    for (let line of body) {
        let match = line.match(pattern);
        if (match == undefined) {
            continue;
        }
        return { type: undefined };
    }
    return undefined;
}
function parseRaises(body) {
    let raises = [];
    let pattern = /raise\s+([\w.]+)/;
    for (let line of body) {
        let match = line.match(pattern);
        if (match == undefined) {
            continue;
        }
        raises.push({ exception: match[1] });
    }
    return raises;
}
function inArray(item, array) {
    return array.some(x => item == x);
}
exports.inArray = inArray;
//# sourceMappingURL=parse_parameters.js.map
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const utilities_1 = require("./utilities");
function getDefinition(document, linePosition) {
    let lines = document.split('\n');
    let definition = "";
    if (linePosition == 0) {
        return definition;
    }
    let currentLineNum = linePosition - 1;
    let originalIndentation = utilities_1.indentationOf(lines[currentLineNum]);
    while (currentLineNum >= 0) {
        let line = lines[currentLineNum];
        definition = line.trim() + definition;
        if (utilities_1.indentationOf(line) < originalIndentation || utilities_1.blankLine(line)) {
            break;
        }
        ;
        currentLineNum -= 1;
    }
    return definition;
}
exports.getDefinition = getDefinition;
function getBody(document, linePosition) {
    let lines = document.split('\n');
    let body = [];
    let currentLineNum = linePosition;
    let originalIndentation = utilities_1.indentationOf(lines[currentLineNum]);
    while (currentLineNum < lines.length) {
        let line = lines[currentLineNum];
        if (utilities_1.blankLine(line)) {
            currentLineNum++;
            continue;
        }
        ;
        if (utilities_1.indentationOf(line) < originalIndentation) {
            break;
        }
        ;
        body.push(line.trim());
        currentLineNum++;
    }
    return body;
}
exports.getBody = getBody;
//# sourceMappingURL=get_lines.js.map
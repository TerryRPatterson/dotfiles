"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const utilities_1 = require("./utilities");
function docstringIsClosed(document, linePosition, charPosition, quoteStyle) {
    let lines = document.split('\n');
    if (quotesCloseExistingDocstring(lines, linePosition, charPosition, quoteStyle)) {
        return true;
    }
    if (quotesOpenExistingDocstring(lines, linePosition, charPosition, quoteStyle)) {
        return true;
    }
    return false;
}
exports.docstringIsClosed = docstringIsClosed;
function quotesCloseExistingDocstring(lines, linePosition, charPosition, quoteStyle) {
    let linesBeforePosition = sliceUpToPosition(lines, linePosition, charPosition);
    let numberOfTripleQuotes = 0;
    for (let line of linesBeforePosition.reverse()) {
        if (line.includes('def ') || line.includes('class ')) {
            break;
        }
        ;
        numberOfTripleQuotes += occurrences(line, quoteStyle);
    }
    return (numberOfTripleQuotes % 2 == 0);
}
function quotesOpenExistingDocstring(lines, linePosition, charPosition, quoteStyle) {
    let linesAfterPosition = sliceFromPosition(lines, linePosition, charPosition);
    let originalIndentation = utilities_1.indentationOf(lines[linePosition]);
    // Need to check first line separately because indentation was sliced off
    if (linesAfterPosition[0].includes(quoteStyle)) {
        return true;
    }
    for (let line of linesAfterPosition.slice(1)) {
        if (line.includes(quoteStyle)) {
            return true;
        }
        if ((!utilities_1.blankLine(line) && utilities_1.indentationOf(line) < originalIndentation) ||
            (line.includes('def ') || line.includes('class '))) {
            return false;
        }
        ;
    }
    return false;
}
function sliceUpToPosition(lines, linePosition, charPosition) {
    let slicedDocument = lines.slice(0, linePosition);
    slicedDocument.push(lines[linePosition].slice(0, charPosition));
    return slicedDocument;
}
function sliceFromPosition(lines, linePosition, charPosition) {
    let slicedDocument = [lines[linePosition].slice(charPosition)];
    slicedDocument = slicedDocument.concat(lines.slice(linePosition + 1));
    return slicedDocument;
}
function occurrences(string, word) {
    return string.split(word).length - 1;
}
//# sourceMappingURL=closed_docstring.js.map
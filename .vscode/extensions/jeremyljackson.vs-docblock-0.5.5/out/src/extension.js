/**
 * Extension entry point
 */
'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode_1 = require("vscode");
// Handles the '/** + enter' action before the code parsing begins
const snippets_1 = require("./snippets");
// Auto-completion rules
const rules_1 = require("./rules");
// Language specific code parsers
const java_1 = require("./languages/java");
const javascript_1 = require("./languages/javascript");
const php_1 = require("./languages/php");
const scss_1 = require("./languages/scss");
const typescript_1 = require("./languages/typescript");
function activate(context) {
    // Associative list of allowed languages
    // Scheme as follows:
    //   language ID: class name
    const langList = {
        java: java_1.Java,
        javascript: javascript_1.JavaScript,
        php: php_1.PHP,
        scss: scss_1.Scss,
        typescript: typescript_1.TypeScript,
    };
    // Register each language
    for (const language in langList) {
        if (langList.hasOwnProperty(language)) {
            // Get language parser object from list
            const parser = new langList[language]();
            // Create snippet object with the parser above
            const snippet = new snippets_1.Snippets(parser);
            // Register docblockr auto competition
            let disposable = vscode_1.languages.registerCompletionItemProvider(language, snippet, '*', '@');
            context.subscriptions.push(disposable);
            // List of classes that doesn't have docblock auto-completion supported
            const autoComplete = [
                'java',
                'scss',
            ];
            if (autoComplete.some((item) => item === language)) {
                // Create language configuration object for adding enter rules
                const config = {
                    onEnterRules: [],
                };
                // Pull enter rules defined by Rules object to autocomplete *
                rules_1.Rules.enterRules.map((rule) => {
                    config.onEnterRules.push(rule);
                });
                // Set up configuration per language
                disposable = vscode_1.languages.setLanguageConfiguration(language, config);
                context.subscriptions.push(disposable);
            }
        }
    }
}
exports.activate = activate;
//# sourceMappingURL=extension.js.map
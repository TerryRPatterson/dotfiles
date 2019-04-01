"use strict";
/**
 * Per language parser settings
 */
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * Object of language specific settings
 */
class Settings {
    /**
     * Dynamically updates class properties based on options object
     *
     * @param  {Options}  options  Options specific to language
     */
    constructor(options = {}) {
        /**
         * Start of a doc block
         */
        this.commentOpen = '/**';
        /**
         * End of a doc block
         */
        this.commentClose = ' */';
        /**
         * End of doc block string
         */
        this.eos = '\n';
        /**
         * Grammar definitions for language
         */
        this.grammar = {
            class: '',
            function: '',
            identifier: '',
            modifiers: [''],
            types: [''],
            variables: [''],
        };
        /**
         * The beginning set of characters for a doc block
         */
        this.separator = ' * ';
        // Loop over options
        for (const option in options) {
            // Check if option exists in settlings
            if (this.hasOwnProperty(option)) {
                // Apply option to settings
                this[option] = options[option];
            }
        }
    }
}
exports.Settings = Settings;
//# sourceMappingURL=settings.js.map
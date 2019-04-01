"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const languageModelCache_1 = require("./languageModelCache");
const embeddedSupport_1 = require("./embeddedSupport");
const vue_1 = require("./vue");
const style_1 = require("./style");
const javascript_1 = require("./script/javascript");
const template_1 = require("./template");
const stylus_1 = require("./style/stylus");
class LanguageModes {
    constructor() {
        this.modes = {};
        this.documentRegions = languageModelCache_1.getLanguageModelCache(10, 60, document => embeddedSupport_1.getDocumentRegions(document));
        this.modelCaches = [];
        this.modelCaches.push(this.documentRegions);
    }
    init(workspacePath, services) {
        return __awaiter(this, void 0, void 0, function* () {
            const vueHtmlMode = template_1.getVueHTMLMode(this.documentRegions, workspacePath, services.infoService);
            const jsMode = yield javascript_1.getJavascriptMode(this.documentRegions, workspacePath, services.infoService, services.dependencyService);
            this.modes['vue'] = vue_1.getVueMode();
            this.modes['vue-html'] = vueHtmlMode;
            this.modes['css'] = style_1.getCSSMode(this.documentRegions);
            this.modes['postcss'] = style_1.getPostCSSMode(this.documentRegions);
            this.modes['scss'] = style_1.getSCSSMode(this.documentRegions);
            this.modes['less'] = style_1.getLESSMode(this.documentRegions);
            this.modes['stylus'] = stylus_1.getStylusMode(this.documentRegions);
            this.modes['javascript'] = jsMode;
            this.modes['tsx'] = jsMode;
            this.modes['typescript'] = jsMode;
        });
    }
    getModeAtPosition(document, position) {
        const languageId = this.documentRegions.get(document).getLanguageAtPosition(position);
        if (languageId) {
            return this.modes[languageId];
        }
        return null;
    }
    getModesInRange(document, range) {
        return this.documentRegions
            .get(document)
            .getLanguageRanges(range)
            .map(r => {
            return {
                start: r.start,
                end: r.end,
                mode: this.modes[r.languageId],
                attributeValue: r.attributeValue
            };
        });
    }
    getAllModesInDocument(document) {
        const result = [];
        for (const languageId of this.documentRegions.get(document).getLanguagesInDocument()) {
            const mode = this.modes[languageId];
            if (mode) {
                result.push(mode);
            }
        }
        return result;
    }
    getAllModes() {
        const result = [];
        for (const languageId in this.modes) {
            const mode = this.modes[languageId];
            if (mode) {
                result.push(mode);
            }
        }
        return result;
    }
    getMode(languageId) {
        return this.modes[languageId];
    }
    onDocumentRemoved(document) {
        this.modelCaches.forEach(mc => mc.onDocumentRemoved(document));
        for (const mode in this.modes) {
            this.modes[mode].onDocumentRemoved(document);
        }
    }
    dispose() {
        this.modelCaches.forEach(mc => mc.dispose());
        this.modelCaches = [];
        for (const mode in this.modes) {
            this.modes[mode].dispose();
        }
        this.modes = {}; // drop all references
    }
}
exports.LanguageModes = LanguageModes;
//# sourceMappingURL=languageModes.js.map
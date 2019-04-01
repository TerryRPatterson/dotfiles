"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const paths_1 = require("../utils/paths");
class VueInfoService {
    constructor() {
        this.vueFileInfo = new Map();
    }
    init(languageModes) {
        this.languageModes = languageModes;
    }
    updateInfo(doc, info) {
        this.vueFileInfo.set(paths_1.getFileFsPath(doc.uri), info);
    }
    getInfo(doc) {
        this.languageModes.getAllModesInDocument(doc).forEach(m => {
            if (m.updateFileInfo) {
                m.updateFileInfo(doc);
            }
        });
        return this.vueFileInfo.get(paths_1.getFileFsPath(doc.uri));
    }
}
exports.VueInfoService = VueInfoService;
//# sourceMappingURL=vueInfoService.js.map
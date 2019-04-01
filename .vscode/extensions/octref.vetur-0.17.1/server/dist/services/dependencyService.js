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
const path = require("path");
class DependencyService {
    constructor() {
        this.dependencies = {
            prettyhtml: { name: 'prettyhtml', state: 1 /* Unloaded */ },
            eslint: { name: 'eslint', state: 1 /* Unloaded */ },
            eslintPluginVue: { name: 'eslint-plugin-vue', state: 1 /* Unloaded */ },
            jsbeautify: { name: 'js-beautify', state: 1 /* Unloaded */ },
            prettier: { name: 'prettier', state: 1 /* Unloaded */ },
            // prettierEslint: { name: 'prettier-eslint', state: State.Unloaded },
            stylusSupremacy: { name: 'stylus-supremacy', state: 1 /* Unloaded */ },
            typescript: { name: 'typescript', state: 1 /* Unloaded */ }
        };
    }
    init(workspacePath, useWorkspaceDependencies) {
        return __awaiter(this, void 0, void 0, function* () {
            if (!useWorkspaceDependencies) {
                console.log('Using bundled TypeScript 2.8.4.');
                return;
            }
            const workspaceTSPath = path.resolve(workspacePath, 'node_modules/typescript');
            const tsModule = yield Promise.resolve().then(() => require(workspaceTSPath));
            console.log(`Using workspace version of TypeScript ${tsModule.version}.`);
            this.dependencies.typescript = {
                name: 'typecript',
                state: 0 /* Loaded */,
                version: tsModule.version,
                bundled: false,
                module: tsModule
            };
        });
    }
    getDependency(d) {
        if (!this.dependencies[d]) {
            return undefined;
        }
        return this.dependencies[d];
    }
}
exports.DependencyService = DependencyService;
//# sourceMappingURL=dependencyService.js.map
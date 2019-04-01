import { LanguageModelCache } from '../languageModelCache';
import { LanguageMode } from '../languageModes';
import { VueDocumentRegions } from '../embeddedSupport';
import { VueInfoService } from '../../services/vueInfoService';
import { DependencyService } from '../../services/dependencyService';
export declare function getJavascriptMode(documentRegions: LanguageModelCache<VueDocumentRegions>, workspacePath: string | undefined, vueInfoService?: VueInfoService, dependencyService?: DependencyService): Promise<LanguageMode>;

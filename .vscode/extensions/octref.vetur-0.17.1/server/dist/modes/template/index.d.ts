import { LanguageModelCache } from '../languageModelCache';
import { LanguageMode } from '../languageModes';
import { VueDocumentRegions } from '../embeddedSupport';
import { VueInfoService } from '../../services/vueInfoService';
declare type DocumentRegionCache = LanguageModelCache<VueDocumentRegions>;
export declare function getVueHTMLMode(documentRegions: DocumentRegionCache, workspacePath: string | undefined, vueInfoService?: VueInfoService): LanguageMode;
export {};

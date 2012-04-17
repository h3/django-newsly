from modeltranslation.translator import translator, TranslationOptions
from newsly.models import News, NewsPhoto, NewsVideo, NewsDocument

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'teaser', 'body',)
translator.register(News, NewsTranslationOptions)


class NewsPhotoTranslationOptions(TranslationOptions):
    fields = ('title', )
translator.register(NewsPhoto, NewsPhotoTranslationOptions)


class NewsVideoTranslationOptions(TranslationOptions):
    fields = ('title', )
translator.register(NewsVideo, NewsVideoTranslationOptions)


class NewsDocumentTranslationOptions(TranslationOptions):
    fields = ('title', )
translator.register(NewsDocument, NewsDocumentTranslationOptions)

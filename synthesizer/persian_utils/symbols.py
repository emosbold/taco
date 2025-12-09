"""
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
"""
_pad        = "_"
_eos        = "~"
_characters = "ءابتثجحخدذرزسشصضطظعغفقلمنهويِپچژکگیآۀأؤإئًَُّ!(),-.:;?  ̠،…؛؟‌٪#ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_–@+/\u200c"
_other_symbols = ['!', '(', ')', '-', '.', ':', ';', '?']

# Export all symbols:
symbols = [_pad, _eos] + _characters + _other_symbols

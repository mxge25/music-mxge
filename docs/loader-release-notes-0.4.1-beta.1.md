# MXGE Loader 0.4.1-beta.1

Experimental companion. Downloads from supported public links are not yet verified on physical devices.

تحديث لإصلاح مشاكل الروابط والأيقونة والمشاركة:

- محرك الروابط الرسمي yt-dlp 2026.10.21 بدل النسخة المرفقة القديمة 2025.11.12، مع ترقية النسخة المثبتة عند أول استخدام والحفاظ على أي تحديث أحدث.
- إصلاح استبعاد فيديوهات MP4 الصامتة من خيارات التنزيل.
- «مشاركة ← MXGE Loader» تبدأ المعاينة وتفتح اختيارات الجودة والتنزيل تلقائيًا؛ الاختيار والتنزيل النهائي بيدك.
- أيقونة MXGE الأصلية بنسخ PNG للكثافات المختلفة مع adaptive/round/themed icons. عرضها على لانشر الهاتف لم يُتحقق منه بعد.
- رسائل أوضح للحظر المؤقت والتحقق الآلي وصفحات الدخول، وزر تحديث الدعم والمحاولة. Loader لا يطلب حسابًا ولا يضمن تنزيل كل رابط.

**اختبار عملي محدود:** نفس ريل إنستجرام العام فشل بالمحرك القديم، ثم استُخرج ونُزّل بدون حساب بالمحرك الجديد على Windows: H.264 صامت، 720×1280، نحو 5 ثوانٍ، 1.95MB. هذا لا يثبت التنزيل على أندرويد أو نجاح كل روابط إنستجرام.

Install over the existing app: same package `io.github.mxge25.linkaudio` and release signing certificate, version code **5**. Do not uninstall if you want to retain the app-managed library. Android 8+ ARM devices with **4 KiB pages**; **16 KiB-page devices remain unsupported**. Public sites can still restrict requests or require an authenticated session, which this version does not provide. No internal browser, app ads, accounts, analytics or backend.

Android compilation/lint, release signature/identity and package checks are performed separately from device behavior. Player analysis and all **61 existing regression tests passed**; those tests do not cover Loader's native screens/service. No physical Android device is connected.

All three signed APKs, matching Loader-only source ZIP and SHA256SUMS.txt accompany this release. Check their hashes before installation. The companion source includes the pinned official Python-source extractor and licenses. Native Python/QuickJS/FFmpeg dependencies are unchanged; their unresolved exact producing-build provenance remains documented in SOURCES.md. No Player source or signing keys are included. Player remains offline and its source PRIVATE. Previous releases are preserved.

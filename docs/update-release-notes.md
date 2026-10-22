# MXGE Player beta.1 · build 6 + MXGE Links 0.2.0

Not yet verified on physical devices. The cutter is experimental.

## MXGE Player — مشغل الصوت

- أيقونة أصلية جديدة تتكيف مع شكل أيقونات الهاتف.
- إصلاح حذف أيقونات التشغيل من إشعار نسخة التثبيت.
- وصول واضح للتبطئة والتسريع والقص وتعديل بيانات الأغنية داخل المكتبة.
- تطبيق الثيمات الثلاثة على الواجهة: داكن، AMOLED، ولون مخصص.
- يعمل دون إنترنت أو إعلانات أو حسابات. التطبيق المساعد منفصل.

Android 8.0+; ARM64 primary and ARMv7 alternative. Same applicationId and release certificate as the previous signed beta, base version code **6**. Install as an update; avoid uninstalling if you want to retain local data. Export a local backup first. Song labels are stored inside MXGE; embedded tags in original files are unchanged. The home widget remains unimplemented.

Final Flutter analysis is clean and all **61 existing-suite tests** passed. No phone validation of notifications, native audio, cutter output/memory or performance is claimed.

## MXGE Links — مساعد الروابط التجريبي

Experimental companion. Downloads from supported public links are not yet verified on physical devices.

- تطبيق مستقل بأيقونة مختلفة، للصوت M4A أو الفيديو MP4 حتى 720p عند توفر الصيغة المتوافقة.
- لصق رابط أو استقبال المشاركة من يوتيوب وإنستجرام وتيك توك وفيسبوك.
- حفظ الملف في مكان تختاره؛ الصوت يُفتح في MXGE والفيديو في مشغل الفيديو على الهاتف.
- اترك التطبيق ظاهرًا أثناء التحميل. الروابط الخاصة أو المحمية أو التي تحتاج تسجيل دخول قد لا تعمل.
- يحتاج الإنترنت؛ MXGE Player نفسه لا يطلب إذن إنترنت. أذونات المساعد: INTERNET فقط.

Independent applicationId `io.github.mxge25.linkaudio`, version 0.2.0-experimental / code 2. Both ARM APKs compile and pass release lint/signature/manifest/alignment checks. No platform download, audible extraction, video playback, save or cancellation result is claimed device-tested. Devices with 16 KiB memory pages are rejected before loading this experimental runtime because upstream's nested codec binaries have known compatibility limits; Android 8+ alone is not a guarantee for every device.

The companion integration source, Gradle wrapper, lockfile, GPL text and upstream source directions are supplied in the companion-source ZIP. The player source remains PRIVATE and is not in that archive. The upstream runtime is pinned to youtubedl-android 0.18.1; its prebuilt producing-build provenance remains unresolved upstream. The source directions distinguish verified wrapper/tag identity from unverified native producing recipes; no reproducible-native-build claim is made.

Compare downloaded APKs with SHA256SUMS.txt. Old release assets remain available under the earlier tag.

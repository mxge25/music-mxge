# MXGE Loader 0.8.0-beta.1 · code 11

هوية جديدة بالأسود والأبيض ولمسة نحاسي، شعار M أصلي، شاشة رابط/بحث مرتّبة، تنقّل أوضح، واختيار صور وجودات بمكان حفظ ظاهر وزر تنزيل ثابت. صفحة التحميل بنفس الهوية.

إصلاح صور إنستجرام: الاحتفاظ بنتائج الصور الأصلية للمنشورات التي لا تحتوي فيديو، واختيار الملف الأصلي مع معاينة صغيرة مستقلة. فحص منشور ألبوم وصورة منفردة على الكمبيوتر نتج عنه خمس صور JPEG سليمة حتى 4096×4096. الصور لا تتحول إلى أغلفة فيديو. قراءة بيانات الصور الحديثة وأرقام المنشورات وروابط فيسبوك القياسية أكثر مرونة؛ قيود المصدر أو طلب الدخول قد تمنع بعض الروابط.

فحص الجودات لا يكرر طلبات صفحات إنستجرام قبل طلب المحرك، ويحتفظ بنتيجة الرابط خمس دقائق، بمهلة اتصال 8 ثوانٍ ودون إعادة محاولات أثناء الفحص، مع إيقاف الطلب بعد 30 ثانية. سرعة المصدر والهاتف تختلف؛ هذه التحسينات ليست ضمان وقت تحميل ثابت.

الصوت افتراضيًا في **Music/MXGE Loader** ومُسجّل كصوت موسيقي في MediaStore. الفيديو في **Movies/MXGE Loader** والصور في **Pictures/MXGE Loader**. المجلد المخصص يُستخدم فقط عند اختياره، والمهام السابقة تحتفظ بمكانها المحفوظ.

Fresh desktop metadata probes succeeded for the selected YouTube, Instagram, Facebook Watch and X links. Eighteen focused compiled photo-parser checks and eighteen existing audio-policy checks passed; Kotlin compilation/lint/package gates passed. Five original Instagram photos transferred and fully decoded on desktop. Facebook photo network samples returned HTTP 400 in this environment, so live Facebook photo transfer is not verified. Existing audio-track verification and background retries remain.

**Experimental companion. Downloads from supported public links are not yet verified on physical devices.**

ARM64 is the main download; ARMv7 is available for older devices. Same applicationId and signing certificate; install over the existing Loader without uninstalling. ARM/4KiB runtime restriction remains. Player build 10, private Player source, app permissions and prior releases remain unchanged. The download page preview is illustrative, not a phone screenshot. Required notices remain under About → Legal information; companion-only source and checksums accompany this release.

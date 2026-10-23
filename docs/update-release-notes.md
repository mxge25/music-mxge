# MXGE Player build 8 — Library scrolling & visible themes

Not yet verified on physical devices. The cutter is experimental.

إصلاح أساسي: مسار تغليف APK كان يعيد استخدام كود Flutter قديم رغم تحديث الموارد واللوجو. تم تجاوز أداة NDK غير الفعالة، والتحقق أن كود التطبيق داخل نسختي APK يطابق الناتج الحالي للمترجم ويحتوي نصوص الإعدادات الجديدة وbuild 8. فحص التوقيع أو الحجم وحده لم يكن يكشف المشكلة.

شريط سحب جانبي ظاهر للمكتبة: اسحبه للطلوع والنزول في الأغاني والمجلدات والألبومات والفنانين وقوائم التشغيل. الأغنية الحالية مميزة بخلفية وعنوان بلون الثيم وعلامة صوت ثابتة، ويتغير التمييز مع الأغنية ويظل ظاهرًا أثناء الإيقاف المؤقت.

الثيمات الثلاثة ظاهرة مباشرة في أول الإعدادات: داكن، أسود AMOLED، ولون مخصص. مجموعات الإعدادات الخمس وإعدادات الحركة وأدوات الأغنية ما زالت متاحة. يظهر build 8 في الإعدادات للتأكد من النسخة المثبتة.

Android 8+; same application ID and signing certificate. Base code 8: ARM64 2008 / ARMv7 1008. Install as an update; keep a local metadata backup. Entirely offline with no INTERNET permission. App source remains PRIVATE. No feature was removed for APK size.

Persistent draggable library scrollbars follow RTL/LTR. Current-track highlighting follows actual playback selection and remains while paused. Theme choices are directly accessible on the settings landing page, including custom accent controls.

Validation: clean Flutter analysis. The existing 61-test suite ran; all scenarios have passing results after retesting the corrected offscreen layout fixture. Extended existing Arabic/English, portrait/landscape and 1x/2x layout fixtures verify dragging down/up through 120 tracks, changing current-track selection, paused selection and visible theme choices. These are automated widget checks with synthetic data, not phone tests. Installation, hardware audio, notifications, cutter output/memory and performance still need physical-device verification.

This release updates MXGE Player only. Existing MXGE Links releases/downloads remain available unchanged. Compare downloads with SHA256SUMS.txt.

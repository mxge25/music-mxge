# MXGE Player build 10 — الحذف والعشوائي والتشغيل من البداية

- حذف ملف الأغنية الحقيقي من أدوات الأغنية أو قائمة الملف، بعد تأكيدك وموافقة أندرويد عند الحاجة. الإلغاء أو فشل إذن الحذف يحافظان على سجل المكتبة. النسخ المستوردة الخاصة تُحذف كنسخة محلية؛ المستندات المقروءة فقط قد تحتاج اختيارها مجددًا بإذن كتابة أو حذفها من الملفات.
- زر العشوائي بجوار التكرار في شاشة التشغيل العادية والأفقية. يحافظ على تشغيل الأغنية الحالية ويحفظ وضع وترتيب الطابور، مع توافق النسخة الاحتياطية.
- التالي والسابق والسحب واختيار الأغنية والانتقال التلقائي يبدأون من الصفر. «متابعة الاستماع» الصريحة واستعادة الجلسة والعلامات تحفظ مواضعها.

**Not yet verified on physical devices. The cutter is experimental.**

Final Flutter analysis clean. All 68 scenarios have passing results: first run 66 passed / two landscape failures; corrected landscape shuffle and reran all seven existing layout scenarios successfully. The 18-scenario existing repository suite also passed after shuffle backup mapping. No new suite or regression removed. Kotlin/native release build passed. Native deletion system dialogs/providers, audio behavior and device upgrades need phone validation; no attached phone/AVD.

Completely offline, no INTERNET permission or backend. Same applicationId/certificate; base code 10 (ARM64 2010 / ARMv7 1010). Install as an update without uninstalling. Existing releases retained. Player application source stays PRIVATE; public repository is download-page/release distribution only.

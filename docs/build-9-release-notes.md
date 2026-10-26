# MXGE Player build 9

Not yet verified on physical devices. The cutter is experimental.

تحديث المشغّل حسب ملاحظات الاستخدام:

- توزيع أهدأ لشاشة «تستمع الآن»، بصورة أكبر ومساحة موزعة بين بيانات الأغنية والتحكم بدل تجمع الصفحة بالأعلى. الخط الكبير والشاشة الأفقية يظلان قابلين للتمرير.
- زر تكرار ظاهر: إيقاف ← تكرار الكل ← تكرار أغنية واحدة. الاختيار محفوظ، ويعمل مع نهاية الملف والطابور وحالة جلسة الوسائط. تعديل التكرار من إعدادات الملف/المجلد يعيد أولوية الإعدادات التفصيلية.
- المكتبة تفتح افتراضيًا على «المضافة حديثًا» باستخدام تاريخ الإضافة من أندرويد، مع الاحتفاظ بتاريخ استيراد الملفات المحلية عند فتحها مرة أخرى. مواضع الاستماع والمكتبة لا تُحذف.
- طلب الإشعار العادي MAY_DUCK لا يخفض الصوت أو يوقف الأغنية من داخل التطبيق. تظل المكالمات وفقد التركيز الفعلي وفصل السماعة أسبابًا للإيقاف؛ الوقف اليدوي يمنع استئنافًا غير مقصود. التطبيق لا يضمن تجاوز سياسات الصوت التي يفرضها مصنع الهاتف.

Install as an update without uninstalling. Same app ID `io.github.mxge25.player` and signing certificate; version 1.0.0-beta.1, build **9**, ARM64 code **2009** / ARMv7 **1009**. Android 8+. Keep a local metadata backup before updating.

Final analysis is clean. The existing suites were run with three focused cases added to existing files; all **64 scenarios have passing results** after the affected repository/layout cases were repaired and rerun. Arabic/English, 360dp portrait/landscape and 1x/2x text include repeat-button interaction and preserve the prior scrollbar/current-song/theme checks. These use synthetic data and fake audio events; they do not establish phone playback, actual notification volume, call/headset routing or performance. No physical Android phone is connected.

Release packaging verifies current Flutter AOT against the APK, retains all features and allocated native code/data, and checks the existing signature, offline permissions and alignment. Player source remains **PRIVATE**; this release contains APKs and SHA256SUMS only. No account, ads, analytics, backend or INTERNET permission. MXGE Loader and earlier releases are retained. Cutter accuracy/memory/export still needs device testing and remains experimental.

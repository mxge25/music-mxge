# MXGE Loader 0.4.0-beta.1

Experimental companion. Downloads from supported public links are not yet verified on physical devices.

**MXGE Links أصبح MXGE Loader** — تطبيق مستقل بلا إعلانات داخل التطبيق، بالعربية والإنجليزية، دون متصفح داخلي.

- بحث يوتيوب بالاسم، ولصق أو مشاركة روابط عامة مدعومة.
- معاينة الملف واختيار الجودات الفعلية للفيديو MP4 أو الصوت M4A/MP3.
- طابور تنزيل في الخلفية مع إشعارات وإيقاف مؤقت واستكمال وإعادة محاولة وإلغاء. الاستكمال يعتمد على المصدر؛ تجهيز الملف قد يبدأ من جديد.
- مكتبة محلية فيها بحث وفلاتر وتشغيل ومشاركة وإعادة تسمية وحذف، مع اختيار مجلد الحفظ.

ثبّت APK كتحديث لـMXGE Links؛ نفس معرّف التطبيق `io.github.mxge25.linkaudio` ونفس شهادة التوقيع، version code 4. النسخة Universal تضم ARM64 وARMv7. توجد نسخ أصغر لكل معمارية. كل APK أقل من 100,000,000 بايت دون حذف مميزات أو محتويات من المحرك.

**بيتا تجريبية — لم تُختبر على هاتف فعلي.** أندرويد 8 فأحدث، أجهزة ARM بصفحات ذاكرة 4KB فقط. صفحات 16KB غير مدعومة بالمحرك الحالي. نجاح تنزيلات المنصات والتحويل والاستكمال والإشعارات والترميزات يحتاج اختبار هاتف؛ الروابط الخاصة أو المحمية أو المقيدة قد تفشل. البحث بالاسم ليوتيوب فقط. قوائم التشغيل والتشغيل العائم/في الخلفية غير مضافة؛ تشغيل الملفات داخل المكتبة يتوقف عند مغادرة شاشة المشغل.

اختر مجلدًا للاحتفاظ بالملفات خارج التطبيق؛ ملفات مكتبة التطبيق تُحذف مع إزالته. يلزم 512MiB متاحة عند بدء التنزيل، مع مساحة إضافية للتجهيز والحفظ. الحد لكل مسار مصدر معلوم الحجم 1GiB؛ المسارات مجهولة الحجم قد تتجاوزه. بعد إيقاف العملية أو إعادة تشغيل الهاتف، افتح Loader واستكمل المهام المحفوظة يدويًا.

Validation: Android release compilation, lint and APK identity/signature/alignment/payload verification passed. All 61 existing Player regression tests passed; these do not test the Kotlin Loader service or phone behavior. No companion automated behavior suite or physical-device success is claimed.

The companion-only GPL application-source ZIP contains the matching Loader Kotlin/UI/build code, wrapper, lockfile, GPL/font licenses and SOURCES.md. **No Player source or signing credentials are included.** The pinned prebuilt native runtime's exact producing-build provenance remains unresolved; this application-source archive is not claimed to reconstruct every third-party native build. See SOURCES.md for source directions and limits.

MXGE Player remains entirely offline and its source PRIVATE. Existing Player and MXGE Links releases are retained. Compare every APK and the source ZIP against **SHA256SUMS.txt**.

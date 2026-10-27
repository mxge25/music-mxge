# MXGE Loader 0.6.0-beta.1 · ملفاتك في الجاليري

واجهة أبسط: لصق مباشر، صفوف ملفات مختصرة، فلاتر واضحة وخيارات مرتبة. لوجو أصلي جديد بعلامة شريط الحفظ، مع أيقونات عادية ودائرية وأحادية اللون.

الفيديوهات الجديدة تُحفظ افتراضيًا في **Movies/MXGE Loader** عبر MediaStore، والصوت في **Music/MXGE Loader**. من **ملفاتي ← إظهار الملفات القديمة في الجاليري** تقدر تنقل تنزيلات النسخ السابقة بأمان؛ الأصل يفضل موجود لو النسخ فشل. اختيار مجلد مخصص ما زال متاحًا، وظهوره بالجاليري يعتمد على المجلد.

Default public media output replaces private app storage. The completed file is published after copying; old private files can be exported sequentially without deleting originals on failure. Android 10+ requires no storage permission for these owned media rows. Android 8/9 request the legacy write grant only when needed, capped at API 28.

Update over the current Loader/Links install; preserve the same applicationId/certificate. Do not uninstall before exporting older private files. Existing releases are retained; Player remains offline and its source stays private. APKs, companion-only source ZIP and SHA256SUMS.txt accompany this release.

**Experimental companion. Downloads from supported public links are not yet verified on physical devices.**

Build/lint/signature checks do not prove OEM Gallery indexing, native UI, cross-app or notification behavior. No Android device/AVD was available. ARM Android 8+ with 4KiB memory pages; this pinned runtime does not support 16KiB pages. Source streams/temporary output need free space. Login-only/protected/changed sources can fail; no app ads, account collection or embedded browser. Native provenance limits and GPL notices are in the companion source ZIP's SOURCES.md.

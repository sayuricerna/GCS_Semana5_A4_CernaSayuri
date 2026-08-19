# SRS v1 

REQ-001: El sistema permitirá listar productos.
REQ-002: El sistema permitirá agregar productos con cantidad >= 0.
RNF-001: Los cambios deben ser trazables a un ISSUE y evidencias.
RNF-002: Versionado seguirá SemVer con tags y changelog.

REQ-003: El sistema permitirá filtrar productos por fecha de registro.
Criterio de aceptación: acepta un rango (fecha_inicio, fecha_fin) y devuelve
solo los productos registrados dentro de ese rango. Estado: registrado,
pendiente de implementación (ver CM_STATUS_REGISTER.md).
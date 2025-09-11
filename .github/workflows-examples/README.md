# 📚 Workflows de Ejemplo para GH-200

Esta carpeta contiene workflows de ejemplo que demuestran diferentes conceptos de GitHub Actions para el examen GH-200. Estos workflows están **desactivados** (no se ejecutan) pero sirven como referencia y ejemplos de estudio.

## 📋 Workflows Incluidos

### 🔨 `build-and-test.yml`
- **Concepto**: Build y testing con matrix strategy
- **Características**:
  - Matrix builds (Python 3.8-3.11)
  - Caching de dependencias
  - Cobertura de código
  - Artifacts de reportes
  - Codecov integration

### 🚀 `deploy-development.yml`
- **Concepto**: Despliegue automático a development
- **Características**:
  - Trigger en workflow_run
  - Environment protection
  - Artifact download
  - Smoke testing

### 🎭 `deploy-staging.yml`
- **Concepto**: Despliegue a staging con validaciones
- **Características**:
  - Pre-deploy checks
  - Security scanning
  - Integration testing
  - Force deploy option

### 🏭 `deploy-production.yml`
- **Concepto**: Despliegue a producción con tags
- **Características**:
  - Tag-based deployment
  - Release validation
  - Rollback support
  - Critical validations
  - Pre-release detection

### 🏷️ `create-release.yml`
- **Concepto**: Creación automática de releases
- **Características**:
  - Manual workflow dispatch
  - Version validation
  - Automatic release notes
  - Tag creation
  - GitHub release creation

### 📋 `info-demo.yml`
- **Concepto**: Demostración de contextos y tokens
- **Características**:
  - GitHub context variables
  - Environment variables
  - Conditional execution
  - JSON output
  - Debug mode

### 🚀 `deploy-with-artifacts.yml`
- **Concepto**: Despliegue multi-entorno con artefactos
- **Características**:
  - Artifact reuse
  - Multi-environment deployment
  - Environment-specific configuration
  - Manual deployment

## 🎯 Conceptos de GH-200 Cubiertos

### ✅ **Triggers**
- `push` con filtros de ramas
- `pull_request`
- `workflow_dispatch` con inputs
- `workflow_run` dependencies
- `tags` patterns

### ✅ **Jobs y Steps**
- Job dependencies (`needs`)
- Conditional execution (`if`)
- Matrix strategies
- Parallel execution
- Sequential workflows

### ✅ **Artifacts y Caching**
- Upload/download artifacts
- Dependency caching
- Cross-job data transfer
- Retention policies

### ✅ **Environments**
- Environment protection
- Environment URLs
- Environment-specific secrets
- Manual approvals

### ✅ **Security**
- Secret management
- Token usage
- Security scanning
- Vulnerability checks

### ✅ **Advanced Features**
- Custom actions
- Reusable workflows
- Context variables
- Expression syntax
- Output variables

## 📖 Cómo Usar Estos Ejemplos

1. **Para Estudio**: Revisa cada workflow para entender los conceptos
2. **Para Referencia**: Copia patrones específicos a tus workflows
3. **Para Práctica**: Activa temporalmente moviendo a `.github/workflows/`
4. **Para el Examen**: Usa como referencia de sintaxis y mejores prácticas

## 🔄 Workflow Activo Actual

El workflow activo es: `.github/workflows/build-once-deploy-many.yml`

Este workflow implementa la estrategia "Build Once, Deploy Many" siguiendo las mejores prácticas de CI/CD.

---

*Estos ejemplos fueron creados para preparación del examen GH-200 de GitHub Actions*
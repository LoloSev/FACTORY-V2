# RUNTIME_EN_FR_OUTPUT_POLICY

STATUS: ACTIVE
MODE: MACHINE_FIRST_RUNTIME_WITH_NATIVE_FRENCH_PLAYER_OUTPUT

## RULE

Runtime documentation uses canonical English machine-first terms for execution.

Player-facing quiz content remains native French.

## SCOPE_RUNTIME_EN

Applies to:
- RULE
- INPUT
- OUTPUT
- PROCESS
- CONDITION
- VALIDATION
- FAILURE_CASE
- ACCEPTED
- REJECTED
- DEPENDENCY
- EXECUTION
- KNOWLEDGE
- ACTIVE_CONTEXT_COST
- MACHINE_FIRST
- CALCULABLE_VALIDATION

## SCOPE_OUTPUT_FR

Applies to all player-visible content:
- questions
- answers
- explanations
- hints
- wording
- tone
- cultural phrasing
- quiz narration

## FORBIDDEN_PATTERN

Do not generate player-facing quiz content in English and then translate it to French.

Required pattern:
- runtime reasoning may use machine-first English structures
- final player-visible output is generated directly in native French

## ACCEPTANCE_CRITERIA

ACCEPTED if:
- runtime fields use canonical English labels
- player-visible content is native French
- no automatic EN_TO_FR translation step is required for quiz text
- RETEX and ARCHIVE may remain French when outside active execution

REJECTED if:
- player-facing quiz content is English
- quiz text is translated mechanically from English
- runtime labels reintroduce deprecated French execution synonyms

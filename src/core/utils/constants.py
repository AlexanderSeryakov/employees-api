ALL_FILTERS_FIELD = frozenset((
    "name",
    "email",
    "company",
    "job_title",
    "gender",
    "age",
    "salary",
))

STR_MATCHING_FILTERS_FIELD = frozenset((
    "name",
    "email",
    "company",
    "job_title",
    "gender",
))

ORDER_TYPES = frozenset((
    "name",
    "-name",
    "age",
    "-age",
    "salary",
    "-salary"
))

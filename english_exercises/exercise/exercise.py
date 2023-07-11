import attr


@attr.s(auto_attribs=True)
class Exercise:
    # 'raw', 'exercise_type', 'object', 'options', 'answer', 'description'
    raw: str
    exercise_type: str
    exercise_text: str
    options: list[str]
    answer: set[str]
    description: str



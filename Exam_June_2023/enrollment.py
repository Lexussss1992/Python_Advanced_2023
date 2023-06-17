def gather_credits(credits, *args):
    course_dict = {}
    flag = False

    for course, credit in args:
        if course in course_dict.keys():
            continue
        else:
            course_dict[course] = credit

    current_credits = 0
    courses = []

    for key, value in course_dict.items():
        current_credits += value
        if current_credits >= credits:
            flag = True
            courses.append(key)
            break
        else:
            courses.append(key)

    return f'Enrollment finished! Maximum credits: {current_credits}.' + '\n' + f'Courses: {", ".join(str(i) for i in sorted(courses))} ' if current_credits >= credits else f'You need to enroll in more courses! You have to gather {credits - current_credits} credits more.'



# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))
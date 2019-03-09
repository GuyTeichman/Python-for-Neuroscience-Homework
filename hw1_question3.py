def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Each subject is a dictionary. The dictionary contains a key called 'subject',
    whose value is the name of subject. Each other key is the name of the student, 
    with the values being a list of the grades. They are ordered [first_exam,second_exam]
        """
    students=set.intersection(set(subj1_all_students.keys()),set(subj2_all_students.keys()))-{'subject'}
    #turn the list of students in each subject into a set. we then take only
    #students that appear in both sets, by using 'intersection'. 
    #all dictionaries also contain the 'subject' key, so we remove it. 
    for student in students:
        if max(subj1_all_students[student])>max(subj2_all_students[student]):
            print(student,' ',subj1_all_students['subject'])
        else:
            print(student,' ',subj2_all_students['subject'])
    



if __name__ == '__main__':
    # Question 3
    '''
    Each subject is a dictionary. The dictionary contains a key called 'subject',
    whose value is the name of subject. Each other key is the name of the student, 
    with the values being a list of the grades. They are ordered [first_exam,second_exam]
    '''
    math={'subject':'math','Guy Teichman':[100,95],'Pablo Blinder':[86,54],'Dan':[64,88],'John':[92,97],'Spanish Inquisitor':[45,74]}
    history={'subject':'history','Guy Teichman':[83,61],'Pablo Blinder':[79,76],'Asaf':[87,93],'Goni':[96,83],'Spanish Inquisitor':[99,35]}
    compare_subjects_within_student(math,history)


def submit_exam(request, exam_id):
    exam = get_object_or_401(Exam, id=exam_id)
    
    if request.method == 'POST':
 
        return render(request, 'exam_result.html', {'submission': submission})
    
    return render(request, 'exam_submission.html', {'exam': exam})

from flask import Blueprint, render_template, url_for, redirect, request, session


bp = Blueprint('exams', __name__)


@bp.route('/exams',methods=['GET', 'POST'])
def exams():
    marks = []
    if request.method == 'POST':
        
        answer1 = request.form['answer1']
        if answer1 == 'A,B,C,D':
            marks.append(7.69)
        elif answer1 == 'A,B':
            marks.append(3.076)
        elif answer1 == 'A':
            marks.append(1.538)
        elif answer1 == 'B':
            marks.append(1.538)
        else:
            marks.append(4.614)
        
        answer2 = request.form['answer2']
        if answer2 == 'A':
            marks.append(7.69)
        else:
            marks.append(0)
            
        answer3 = request.form['answer3']
        if answer3 == 'C':
            marks.append(7.69)
        else:
            marks.append(0)
            
        answer4 = request.form['answer4']
        if answer4 == 'A,B,D':
            marks.append(7.69)
        else:
            marks.append(0)
            
        answer5 = request.form['answer5']
        if answer5 == 'A,B,C':
            marks.append(7.69)
        else:
            marks.append(0)
            
        answer6 = request.form['answer6']
        if answer6 == 'A,D':
            marks.append(7.69)
        else:
            marks.append(0)
        
        answer7 = request.form['answer7']
        if answer7 == 'C':
            marks.append(7.69)
        else:
            marks.append(0)
            
        answer8 = request.form['answer8']
        if answer8 == 'B':
            marks.append(7.69)
        else:
            marks.append(0)
            
        answer9 = request.form['answer9']
        if answer9 == 'A':
            marks.append(7.69)
        else:
            marks.append(0)
            
        answer10 = request.form['answer10']
        if answer10 == 'E':
            marks.append(7.69)
        else:
            marks.append(0)
            
        answer11 = request.form['answer11']
        if answer11 == 'A':
            marks.append(7.69)
        else:
            marks.append(0)
            
        answer12 = request.form['answer12']
        if answer12 == 'A':
            marks.append(7.69)
        else:
            marks.append(0)
            
        answer13 = request.form['answer13']
        if answer13 == 'A':
            marks.append(7.69)
        else:
            marks.append(0)
        
        total_marks = sum(marks) #89.67999999999999
        print(total_marks)
        return render_template('exams/marks.html',total_marks=total_marks)
        
    return render_template('exams/final_exams.html')

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib import messages

def list_students(request):
    # Get search parameters from URL
    search = request.GET.get('search', '')
    course_filter = request.GET.get('course', '')
    sort_by = request.GET.get('sort', 'name')  # Default sort by name
    
    # Start with all students
    students = Student.objects.all()
    
    # Get unique courses for dropdown
    courses = Student.objects.values_list('course', flat=True).distinct()
    
    # Filter by search term if provided
    if search:
        students = students.filter(firstname__icontains=search) | students.filter(lastname__icontains=search) | students.filter(email__icontains=search)
        
    # Filter by course if provided    
    if course_filter:
        students = students.filter(course=course_filter)

    # Apply sorting
    if sort_by == 'name':
        students = students.order_by('firstname', 'lastname')
    elif sort_by == 'id':
        students = students.order_by('StudentID')
    elif sort_by == 'course':
        students = students.order_by('course')
    elif sort_by == 'email':
        students = students.order_by('email')
    elif sort_by == 'dob':
        students = students.order_by('dateofbirth')
    elif sort_by == 'enrollment':
        students = students.order_by('enrollmentdate')

    # Show all students in template
    return render(request, 'list_students.html', {
        'students': students,
        'courses': courses,
        'current_sort': sort_by  # Pass the current sort to highlight the selected option
    })

def add_student(request):
    # Get unique courses for dropdown
    courses = Student.objects.values_list('course', flat=True).distinct()
    
    if request.method == 'POST':
        try:
            # Get form data with correct field names
            student = Student.objects.create(
                StudentID=request.POST.get('student_id'),
                firstname=request.POST.get('firstname'),
                lastname=request.POST.get('lastname'),
                email=request.POST.get('email'),
                dateofbirth=request.POST.get('dob'),
                course=request.POST.get('course'),
                enrollmentdate=request.POST.get('enrollment_date')
            )
            messages.success(request, 'Student added successfully!')
            return redirect('list_students')
        except Exception as e:
            messages.error(request, f'Error adding student: {str(e)}')
            return render(request, 'add_new_student_form.html', {'error': str(e), 'courses': courses})
            
    return render(request, 'add_new_student_form.html', {'courses': courses})

def edit_student(request, student_id):
    student = get_object_or_404(Student, StudentID=student_id)
    # Get unique courses for dropdown
    courses = Student.objects.values_list('course', flat=True).distinct()
    
    if request.method == 'POST':
        try:
            # Update student information (without changing StudentID)
            student.firstname = request.POST.get('firstname')
            student.lastname = request.POST.get('lastname')
            student.email = request.POST.get('email')
            student.course = request.POST.get('course')
            student.dateofbirth = request.POST.get('dob')
            student.enrollmentdate = request.POST.get('enrollment_date')
            student.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('list_students')
        except Exception as e:
            messages.error(request, f'Error updating student: {str(e)}')
            return render(request, 'edit_student.html', {
                'student': student, 
                'error': str(e),
                'courses': courses
            })
    
    return render(request, 'edit_student.html', {
        'student': student,
        'courses': courses
    })

def delete_student(request, student_id):
    # Get student
    student = Student.objects.get(StudentID=student_id)
    
    if request.method == 'POST':
        # Delete the student
        student.delete()
        messages.success(request, 'Student deleted!')
        return redirect('list_students')
        
    return render(request, 'delete_confirmation.html', {'student': student})



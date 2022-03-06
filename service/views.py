from service.models import ServiceItem, Order, TeamMember, TrainingService,ConsultancyService
from django.shortcuts import redirect, render


# Create your views here.

def index(request):
    return render(request, 'service/index.html')

def service_Item(request):
    serviceItem = ServiceItem.objects.all()
    return render(request, 'service/item.html', {'serviceItem' : serviceItem})

def detail(request, id):
    service_item = ServiceItem.objects.get(pk = id)
    return render(request, 'service/service-detail.html', {'service_item' : service_item})

def checkOut(request):
    if request.method == "POST":
        items = request.POST.get('items')
        username = request.POST.get('username',"")
        email = request.POST.get('email')
        address = request.POST.get('address')
        location = request.POST.get('location')
        city = request.POST.get('city')
        fax = request.POST.get('fax')
        gridCheck = request.POST.get('gridCheck')
        if gridCheck == 'on':
            gridCheck = True
        order = Order(items=items, username = username, email = email, address = address, 
        location = location, city = city, fax = fax, gridCheck = gridCheck)
        order.save()
        return redirect('upload')

    return render(request, 'service/checkout.html')

def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'service/team-members.html', {'team_members':team_members})


def trainingServices(request):
    
    return render(request, 'service/training-courses.html')


def consultancyServices(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        ProjectDesign_preparation = request.POST.get('project_design')
        if ProjectDesign_preparation == 'on':
            ProjectDesign_preparation = True
        EnvironmentalImpactAssessment = request.POST.get('environmental_impact')
        if EnvironmentalImpactAssessment == 'on':
            EnvironmentalImpactAssessment = True
        FeasibilityStudy = request.POST.get('feasibility_study')
        if FeasibilityStudy == 'on':
            FeasibilityStudy = True
        ProposalPreparation = request.POST.get('Proposal_Preparation')
        if ProjectDesign_preparation == 'on':
            ProjectDesign_preparation = True
        BusinessPlan_preparation = request.POST.get('Business_Plan_preparation')
        if BusinessPlan_preparation == 'on':
            BusinessPlan_preparation = True
        OrganizationalStructure = request.POST.get('Organizational_Structure')
        if OrganizationalStructure == 'on':
            OrganizationalStructure = True
        SalaryScalePreparation = request.POST.get('Salary_Scale_Preparation')
        if SalaryScalePreparation == 'on':
            SalaryScalePreparation = True
        JobEvaluationAndGrading = request.POST.get('JobEvaluationAndGrading')
        if JobEvaluationAndGrading == 'on':
            JobEvaluationAndGrading = True
        StrategicPlanningManagement = request.POST.get('StrategicPlanningManagement')
        if StrategicPlanningManagement == 'on':
            StrategicPlanningManagement = True
        TrainingNeedAssessmentSurvey  = request.POST.get('AssessmentSurvey')
        if TrainingNeedAssessmentSurvey == 'on':
            TrainingNeedAssessmentSurvey = True
        ReformImplementation = request.POST.get('ReformImplementation')
        if ReformImplementation == 'on':
            ReformImplementation = True
        OthersDocumentPreparation = request.POST.get('OthersDocumentPreparation')
        if OthersDocumentPreparation == 'on':
            OthersDocumentPreparation = True


        consultancy_services = ConsultancyService(username = username, email = email, ProjectDesign_preparation = ProjectDesign_preparation,
        EnvironmentalImpactAssessment = EnvironmentalImpactAssessment, FeasibilityStudy = FeasibilityStudy,
        ProposalPreparation = ProposalPreparation, BusinessPlan_preparation = BusinessPlan_preparation,
        OrganizationalStructure = OrganizationalStructure, SalaryScalePreparation = SalaryScalePreparation,
        JobEvaluationAndGrading = JobEvaluationAndGrading, StrategicPlanningManagement = StrategicPlanningManagement,
        TrainingNeedAssessmentSurvey = TrainingNeedAssessmentSurvey, ReformImplementation = ReformImplementation,
        OthersDocumentPreparation = OthersDocumentPreparation)

        consultancy_services.save()
        return redirect('service:index')

    return render(request, 'service/consultancy-services.html')




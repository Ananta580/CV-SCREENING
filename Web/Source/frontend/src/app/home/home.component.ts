import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Guid } from "guid-typescript";
import { NzMessageService, NzUploadChangeParam } from 'ng-zorro-antd';
import { AppData } from '../services/appdata';
import { JobService } from '../services/JobService';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {


  isSpinning = false;
  showResult=false;
  decriptionForm: FormGroup;
  files: any[] = [];
  imageUrl = '';
  jobView={
    name:'',
    degree:[],
    degreeWeight: 0,
    designation: [],
    designationWeight: 0,
    skills: [],
    skillsWeight: 0,
    experienceYear:0,
    experienceYearWeight:0
  }
  listOfDegree: Array<{ label: string; value: string }> = [];
  listOfSelectedDegree = [];
  listOfDesignation: Array<{ label: string; value: string }> = [];
  listOfSelectedDesignation = [];
  listOfSkill: Array<{ label: string; value: string }> = [];
  listOfSelectedSkill = [];

  selectedValue: any;
  isVisible = false;

  finalResult:any[]=[];
  descriptionList = []

  constructor(private fb: FormBuilder, private jobService: JobService, private msg: NzMessageService, private appdata: AppData) {
    this.imageUrl = this.appdata.imageUrl
    this.getJsonJobs();
  }

  ngOnInit(): void {
    this.decriptionForm = this.fb.group({
      "id": [Guid.create(), [Validators.required]],
      "name": ['', [Validators.required]],
      "degree": ['', [Validators.required]],
      "degreeWeight": [0, [Validators.required]],
      "designation": ['', [Validators.required]],
      "designationWeight": [0, [Validators.required]],
      "skills": ['', [Validators.required]],
      "skillsWeight": [0, [Validators.required]],
      "experienceYear":[null, [Validators.required]],
      "experienceYearWeight":[0, [Validators.required]]
    })
  }

  getJsonJobs(){
    this.jobService.getJobs().subscribe((data)=>{
      this.descriptionList=data;
      this.selectedValue=this.descriptionList[0].id.value;
      this.seePopUp();
    })
  }

  showAddModal() {
    this.isVisible = true;
  }

  seePopUp(){
    console.log(this.selectedValue)
    var index=this.descriptionList.findIndex(x=>x.id.value==this.selectedValue);
    this.jobView=this.descriptionList[index];
    console.log(this.jobView)
  }
  
  handleOk() {
    this.decriptionForm.controls.degree.setValue(this.listOfSelectedDegree);
    this.decriptionForm.controls.designation.setValue(this.listOfSelectedDesignation);
    this.decriptionForm.controls.skills.setValue(this.listOfSelectedSkill);
    this.descriptionList.push(this.decriptionForm.value);
    console.log(this.decriptionForm.value)
    this.jobService.saveJobs(this.descriptionList).subscribe((data) => {
      this.msg.success("New Job Added Successfully");
    })
    this.isVisible = false;
  }

  handleCancel() {
    this.isVisible = false;
  }

  handleChange({ file, fileList }: NzUploadChangeParam): void {
    if (file.status == "done") {
      this.msg.success("Files are Accepted");
      this.files.push(file.originFileObj);
    }
  }

  submitForm() {
    console.log(this.selectedValue);
    var selectedJob = this.descriptionList.find(x => x.id.value == this.selectedValue);
    if (this.selectedValue != undefined) {
        this.isSpinning = true;
        const formData = new FormData();
        for (var i = 0; i < this.files.length; i++) {
          formData.append("files[]", this.files[i]);
        }
        this.jobService.uploadPdf(formData).subscribe((data) => {
          this.jobService.processJobs(selectedJob).subscribe((data) => {
            
            this.showResult=true;
            this.files=[];
            this.isSpinning=false;
            this.selectedValue='';
            this.finalResult=data.sort((a, b) => b.weight - a.weight);
            this.finalResult=this.finalResult.slice(0,5)
          })
        })
    }
    else {
      this.msg.error("Please Select a Specific Jobs");
    }
  }

  backToUploadPage(){
    this.showResult=false;
  }

  viewPdf(name){
    window.open(this.jobService.viewPdf(name), "_blank")
  }

}

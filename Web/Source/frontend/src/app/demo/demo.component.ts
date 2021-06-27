import { Component, OnInit } from '@angular/core';
import { NzMessageService, NzUploadChangeParam } from 'ng-zorro-antd';
import { AppData } from '../services/appdata';
import { DemoService } from '../services/demoService';

@Component({
  selector: 'app-demo',
  templateUrl: './demo.component.html',
  styleUrls: ['./demo.component.css']
})
export class DemoComponent implements OnInit {

  files: any[] = [];
  imageUrl = '';
  textValue = '';
  extractedConcept = [];
  linkedConcept = '';
  ontologyGenerated = []
  button = { id: 1, name: "Upload and Convert to Text" }
  constructor(private msg: NzMessageService, private appdata: AppData, private demoService: DemoService) {
    this.imageUrl = this.appdata.imageUrl
  }

  ngOnInit(): void {
  }

  handleChange({ file, fileList }: NzUploadChangeParam): void {
    if (file.status == "done") {
      this.msg.success("Files are Accepted");
      this.files.push(file.originFileObj);
    }
  }

  submitForm() {
    if (this.button.id == 1) {
      if (this.files.length >= 1) {
        const formData = new FormData();
        for (var i = 0; i < this.files.length; i++) {
          formData.append("files[]", this.files[i]);
        }
        this.demoService.uploadPdf(formData).subscribe((data) => {
          this.textValue = data.message;
          this.button.id = 2;
          this.button.name = "Do Concept Extraction"
        })
      }
      else {
        this.msg.error("Please Upload Pdf and Try");
      }
    }

    else if (this.button.id == 2) {
      this.demoService.DoOtherTask().subscribe((data) => {
        this.extractedConcept = data.extractedConcept;
        this.linkedConcept = data.linkedConcept;
        this.ontologyGenerated = data.ontoloyGenerated;
        this.textValue = '';
        this.extractedConcept.forEach((item) => {
          this.textValue = this.textValue + item + ' ,';
        })
        this.button.id = 3;
        this.button.name = "Do Concept Linking";
      })
    }
    else if (this.button.id == 3) {
      console.log(this.linkedConcept)
      this.textValue=this.linkedConcept;
      this.button.id = 4;
      this.button.name = "Generate Ontology"
    }
    else if (this.button.id == 4) {
      this.button.id = 5;
      console.log(this.ontologyGenerated)
      var name=this.ontologyGenerated[0];
      var degree=this.ontologyGenerated[2];
      var designation=this.ontologyGenerated[3];
      var experience=this.ontologyGenerated[4];
      var skill=this.ontologyGenerated[1];
      this.textValue='['+name+' , ['+skill+']'+' , ['+degree+']'+' , ['+designation+'] , '+experience+']'
      this.button.name = "Back to Upload"
    }
    else if (this.button.id == 5) {
      this.button.id = 1;
      this.textValue = '';
      this.button.name = "Upload and Convert to Text"
    }

  }

}

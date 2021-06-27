import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';
import { Observable } from "rxjs";
import { AppData } from "./appdata";

@Injectable({
    providedIn: 'root'
})

export class JobService {
    constructor(private httpClient: HttpClient,
                private appData : AppData) { }

    getJobs():Observable<any>
    {
        let apiUrl = this.appData.apiUrl;
        return this.httpClient.get(`${apiUrl}getjob`);
    }
    saveJobs(model):Observable<any>
    {
        let apiUrl = this.appData.apiUrl;
        return this.httpClient.post(`${apiUrl}savejob`,model);
    }
    uploadPdf(model): Observable<any> {
        console.log("calling")
        let apiUrl = this.appData.apiUrl;
        return this.httpClient.post<any>(`${apiUrl}upload`,model);
    }
    processJobs(model):Observable<any> {
        let apiUrl = this.appData.apiUrl;
        return this.httpClient.post<any>(`${apiUrl}process`,model);
    }
    viewPdf(name){
        let apiUrl = this.appData.apiUrl;
        return `${apiUrl}view?pdf=${name}`
    }
}
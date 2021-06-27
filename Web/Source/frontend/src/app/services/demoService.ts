import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';
import { Observable } from "rxjs";
import { AppData } from "./appdata";

@Injectable({
    providedIn: 'root'
})

export class DemoService {
    constructor(private httpClient: HttpClient,
                private appData : AppData) { }

    DoOtherTask():Observable<any>
    {
        let apiUrl = this.appData.apiUrl;
        return this.httpClient.get(`${apiUrl}allsingle`);
    }
    uploadPdf(model): Observable<any> {
        console.log("calling")
        let apiUrl = this.appData.apiUrl;
        return this.httpClient.post<any>(`${apiUrl}uploadsingle`,model);
    }
}
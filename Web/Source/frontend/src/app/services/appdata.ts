import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})

export class AppData{
    apiUrl: string = 'http://127.0.0.1:5100/';
    imageUrl: string = 'https://localhost:44304/image/get';
}
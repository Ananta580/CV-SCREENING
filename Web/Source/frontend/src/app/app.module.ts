import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NzTableModule } from 'ng-zorro-antd/table';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IconsProviderModule } from './icons-provider.module';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { NzUploadModule } from 'ng-zorro-antd/upload';
import { NzCardModule } from 'ng-zorro-antd/card';
import { NzMenuModule } from 'ng-zorro-antd/menu';
import { NzPopoverModule } from 'ng-zorro-antd/popover';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NZ_I18N } from 'ng-zorro-antd/i18n';
import { en_US } from 'ng-zorro-antd/i18n';
import { registerLocaleData } from '@angular/common';
import en from '@angular/common/locales/en';
import { HomeComponent } from './home/home.component';
import { DemoComponent } from './demo/demo.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { NzButtonModule, NzFormModule, NzInputModule, NzInputNumberModule, NzMessageService, NzModalModule, NzSelectModule } from 'ng-zorro-antd';

registerLocaleData(en);

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    DemoComponent,
    WelcomeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NzTableModule,
    NzUploadModule,
    NzCardModule,
    IconsProviderModule,
    ReactiveFormsModule,
    NzInputNumberModule,
    NzInputModule,
    NzModalModule,
    FormsModule,
    NzLayoutModule,
    NzMenuModule,
    NzPopoverModule,
    NzSelectModule,
    NzFormModule,
    FormsModule,
    HttpClientModule,
    NzButtonModule,
    BrowserAnimationsModule
  ],
  providers: [{ provide: NZ_I18N, useValue: en_US },NzMessageService],
  bootstrap: [AppComponent]
})
export class AppModule { }

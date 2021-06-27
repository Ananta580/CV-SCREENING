import { NgModule } from '@angular/core';
import { NZ_ICONS, NzIconModule } from 'ng-zorro-antd/icon';

import {
  MenuFoldOutline,
  MenuUnfoldOutline,
  EnterOutline,
  FormOutline,
  DashboardOutline,
  HomeOutline,
  DownloadOutline,
  PlusOutline,
  SyncOutline,
  InboxOutline,
  EyeOutline,
  BackwardOutline,
  PieChartOutline
} from '@ant-design/icons-angular/icons';

const icons = [MenuFoldOutline,DownloadOutline, MenuUnfoldOutline, EnterOutline, PlusOutline,SyncOutline,InboxOutline, DashboardOutline, EyeOutline, FormOutline, PieChartOutline, BackwardOutline, HomeOutline];

@NgModule({
  imports: [NzIconModule],
  exports: [NzIconModule],
  providers: [
    { provide: NZ_ICONS, useValue: icons }
  ]
})
export class IconsProviderModule {
}

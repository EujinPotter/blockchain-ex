import { Component, OnInit } from '@angular/core';
import { routesConsts } from '../../../consts';
import { Router } from '@angular/router';
import { DeviceDetectorService } from 'ngx-device-detector';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  public isAssets = this.router.url.split('/')[1] === 'assets';
  public isMobile = this.deviceService.isMobile();
  
  constructor(private router: Router, private deviceService: DeviceDetectorService) { }

  ngOnInit(): void {}

  assetsClicked(): void {
    this.router.navigate([routesConsts.CONFIDENTIAL_ASSETS_LIST]);
  }
}

import { NgModule } from '@angular/core';
import { Routes, RouterModule, Router } from '@angular/router';
import { MainComponent, BlockDetailsComponent, ContractDetailsComponent } from './containers';
import { HeaderComponent } from '../../shared/components';
import { MainLayoutComponent } from '../../shared/layouts';

const routes: Routes = [{
  path: '',
  component: MainLayoutComponent,
  children: [{
    path: '',
    children: [
        {
            path: '', component: HeaderComponent, outlet: 'header'
        }, {
            path: '', component: MainComponent
        }
    ]
  }, {
    path: 'block',
    children: [
        {
            path: '', component: HeaderComponent, outlet: 'header'
        }, {
            path: '', component: BlockDetailsComponent
        }
    ]
  }, {
    path: 'block/:hash',
    children: [
        {
            path: '', component: HeaderComponent, outlet: 'header'
        }, {
            path: '', component: BlockDetailsComponent
        }
    ]
  }, {
    path: 'contract/:cid',
    children: [
        {
            path: '', component: HeaderComponent, outlet: 'header'
        }, {
            path: '', component: ContractDetailsComponent
        }
    ]
  }]
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
  providers: []
})
export class HomepageRoutingModule {}

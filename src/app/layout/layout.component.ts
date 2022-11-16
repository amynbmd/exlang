import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-layout',
  templateUrl: './layout.component.html',
  styleUrls: ['./layout.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LayoutComponent implements OnInit {
  constructor(private _router: Router) {}

  ngOnInit(): void {}

  viewTheme() {
    this._router.navigate(['theme', 'view']);
  }

  viewCommunity() {
    this._router.navigate(['community']);
  }
}

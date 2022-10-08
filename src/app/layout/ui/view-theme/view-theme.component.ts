import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-view-theme',
  templateUrl: './view-theme.component.html',
  styleUrls: ['./view-theme.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ViewThemeComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}

using Autofac;
using Autofac.Core;
using RegistrationBook.ViewModels;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RegistrationBook.Data
{
    public class RecordViewModelFactory : IRecordFactory
    {
        private IService _service;
        private IWindowService _windowService;
        private MainWindowViewModel _mainWindowViewModel;

        public RecordViewModelFactory(IService service, IWindowService windowService, MainWindowViewModel mainWindowViewModel)
        {
            _service = service;
            _windowService = windowService;
            _mainWindowViewModel = mainWindowViewModel;
        }

        public RecordViewModel GetRecordViewModel()
        {
            return new RecordViewModel(_service, _mainWindowViewModel);
        }
    }
}
